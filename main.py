from vectorstore import vectorstore
from retriever import retriever
from template import prompt_template
from llm import llm

# Example usage (you can modify it according to your specific needs)
def main():
    question = "Enter your question here"
    
    # Format the prompt with the question
    prompt = prompt_template.format(question=question)
    
    # Use the retriever to get relevant documents
    relevant_docs = retriever.get_relevant_documents(question)
    
    # Generate the answer using the language model
    response = llm(prompt, relevant_docs)
    
    print("Response:", response)

if __name__ == "__main__":
    main()
