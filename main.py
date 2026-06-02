from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")

docs = loader.load()

print(type(docs))
print(len(docs))
print(docs[0])