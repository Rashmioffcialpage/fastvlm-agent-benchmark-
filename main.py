import time
from PIL import Image
from transformers import pipeline
import json

# Load models (simple for demo)
caption_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
qa_model = pipeline("text-generation", model="gpt2")

def process(image_path, question):
    start = time.time()

    image = Image.open(image_path)

    # Step 1: Caption (simulate vision understanding)
    caption = caption_model(image)[0]['generated_text']

    # Step 2: Combine with question
    prompt = f"Image description: {caption}. Question: {question}. Answer:"

    # Step 3: Generate answer
    answer = qa_model(prompt, max_length=50)[0]['generated_text']

    end = time.time()

    latency = end - start

    return answer, latency

def run():
    with open("dataset.json") as f:
        data = json.load(f)

    for item in data:
        ans, lat = process(item["image"], item["question"])

        print("Question:", item["question"])
        print("Predicted:", ans)
        print("Latency:", round(lat, 3), "seconds")
        print("-" * 50)

if __name__ == "__main__":
    run()
