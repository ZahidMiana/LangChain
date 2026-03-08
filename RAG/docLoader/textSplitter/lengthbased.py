from langchain_text_splitters import CharacterTextSplitter

text = "This is a sample text that we will split into smaller chunks based on character length. " * 10

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=" "
)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1} ({len(chunk)} chars):\n{chunk}")