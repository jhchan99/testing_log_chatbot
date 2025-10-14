import actions.StoreEmbeddings as EmbeddingStore


def main():
    # get data
    store_embeddings = EmbeddingStore.EmbeddingStore()
    # vector store
    store_embeddings.add_documents(["Hello, world!"])
    # query the vector store
    results = store_embeddings.query("Hello, world!")
    print(results)


if __name__ == "__main__":
    main()
