# shugaze

![Alt text](./screenshots/screenshot.png)

A shoe price predictor that leverages generative AI with large language models and deep learning to help consumers save money when shopping.

## Tech stack

The frontend is written in `SvelteKit`, and uses `Material Icons`.

The backend is written in `Python` using `fastapi` in `backend/main.py`:

- In `backend/scraper.py`, the `playwright` package is used scrape data from stockx to get our data, which is saved in `data/dataset.csv`
- In `backend/gpt.py`, the `openai` package is used to interface with LLMs to find similar shoes
- In `backend/train_2.py`, the `sklearn` package is used to train a `RandomForestRegressor` on our data to predict future prices of individual shoes

## Usage

### Required tools

Install

- `npm` for JavaScript package management
- `uv` for Python package management
- `node.js` and `python`

### Running

First, clone the repository.

To start the backend, run:

```bash
cd backend
uv run fastapi dev --port 8000
```

To start the frontend, run:

```bash
cd frontend
npm i
npm run dev
```

To generate similar shoes on-the-fly, add your openai key in `secrets.py` as the variable `the_key`, and change `get_similar_shoes_test` in `main.py` to `get_similar_shoes`.

When both are running, you can view the working website at [http://localhost:4242/](http://localhost:4242/).
