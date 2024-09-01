# Customer Support Agent Tutorial Episode 2

In this part of the tutorial we created a vector database with [ChromaDB](https://www.trychroma.com/), and connected it to our streamlit frontend. With this setup we were able to ask FAQ style questions and also ask for product recommendations for our Flower Shop. Within the chroma database we created two knowledge base collections:

- FAQ Question and Answer pairs
- Product descriptions

We also updated the front end to choose between which knowledge base to query:

![image](https://github.com/user-attachments/assets/066caf10-d773-4481-b07b-4d74fafedca2)


## Setup

To setup the python environment I did:

```bash
conda create -p ./.conda python=3.11
pip install -r requirements.txt
```

Then activated the environment with:
```bash
conda activate ./.conda
```

To run the frontend you can type:

```bash
streamlit run streamlit_frontend.py
```

Happy Agent Building :D
