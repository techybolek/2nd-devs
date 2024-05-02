import { TextLoader } from "langchain/document_loaders/fs/text";
import { OpenAIEmbeddings } from "langchain/embeddings/openai";
import { v4 as uuidv4 } from 'uuid';
import { QdrantClient } from '@qdrant/js-client-rest';
import { getTask, submitTask } from "./task_util";
import { extractLinksToMetadata } from "../24_files/helpers";


const COLLECTION_NAME = "c3_l4";
const embeddings = new OpenAIEmbeddings({ maxConcurrency: 5 });
const qdrant = new QdrantClient({ url: process.env.QDRANT_URL });


const result = await qdrant.getCollections();
const indexed = result.collections.find((collection) => collection.name === COLLECTION_NAME);
console.log(result);


// Create collection if not exists
if (!indexed) {
    console.log("Collection doesn't exist, creating....")
    await qdrant.createCollection(COLLECTION_NAME, { vectors: { size: 1536, distance: 'Cosine', on_disk: true } });
}

const collectionInfo = await qdrant.getCollection(COLLECTION_NAME);
// Index documents if not indexed
if (!collectionInfo.points_count) {
    console.log("Collection empty, populating....")

    const SOURCE_DATA_FILE = '/mnt/c/temp/archiwum_aidevs.json'
    // Read File
    const loader = new TextLoader(SOURCE_DATA_FILE);
    let [memory] = await loader.load();
    //let documents = memory.pageContent.split("\n\n").map((content) => (new Document({ pageContent: content })));
    let documents = JSON.parse(memory.pageContent)
    console.log(documents)
    console.log(documents.length, typeof documents)

    // Add metadata
    documents = documents.map((srcDoc: any) => {
        console.log('DOCUMENT', srcDoc)
        const transformedDoc = {
            pageContent: srcDoc.info,
            metadata: {
                source: COLLECTION_NAME,
                content: srcDoc,
                uuid: uuidv4()
            }
        }
        return transformedDoc;
    });

    // Generate embeddings
    const points = [];
    for (const document of documents) {
        console.log('PAge Content:', document.pageContent)
        const [embedding] = await embeddings.embedDocuments([document.pageContent]);
        points.push({
            id: document.metadata.uuid,
            payload: document.metadata,
            vector: embedding,
        });
    }

    // Index
    await qdrant.upsert(COLLECTION_NAME, {
        wait: true,
        batch: {
            ids: points.map((point) => (point.id)),
            vectors: points.map((point) => (point.vector)),
            payloads: points.map((point) => (point.payload)),
        },
    })
}


const { theTask, taskToken } = await getTask("search")
console.log('THE TASK:', theTask)

const queryEmbedding = await embeddings.embedQuery(theTask);

const searchResult = await qdrant.search(COLLECTION_NAME, {
    vector: queryEmbedding,
    limit: 1,
    filter: {
        must: [
            {
                key: 'source',
                match: {
                    value: COLLECTION_NAME
                }
            }
        ]
    }
});

console.log('Search returned:', searchResult);
if (searchResult.length > 0) {
    console.log(searchResult[0].payload?.content);
    //@ts-ignore
    const theAnswer = searchResult[0].payload?.content.url
    submitTask(theAnswer, taskToken)
}