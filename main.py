import time
from PIL import Image # type: ignore
from transformers import pipeline # type: ignore
import json

# Load models
caption_model = pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")
qa_model = pipeline("text-generation", model="gpt2")


def process(image_path, question):
    start = time.time()

    # Open image properly
    image = Image.open(image_path).convert("RGB")

    # Step 1: Generate caption (FIXED HERE ✅)
    caption = caption_model({
        "images": image,
        "text": "Describe the image"
    })[0]['generated_text']

    # Step 2: Combine with question
    prompt = f"Image description: {caption}. Question: {question}. Answer:"

    # Step 3: Generate answer
    answer = qa_model(prompt, max_new_tokens=30, do_sample=False)[0]['generated_text']

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
