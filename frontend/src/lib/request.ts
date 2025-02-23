import type {
  AnalyzeRequest,
  AnalyzeResponse,
  SearchRequest,
  Shoe,
} from "./model";

export async function similar(name: string): Promise<string[]> {
  let res = await fetch("http://127.0.0.1:8000/similar", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: "Laptop",
    }),
  });
  return (await res.json()).similar;
}

export async function analyze(
  request: AnalyzeRequest
): Promise<AnalyzeResponse> {
  return await fetchJson("analyze", "post", request);
}

export async function search(request: SearchRequest): Promise<Shoe[]> {
  return await fetchJson("search", "post", request);
}

export async function trending(): Promise<Shoe[]> {
  return await fetchJson("trending", "get");
}

async function fetchJson(
  path: string,
  method: "get" | "post",
  json: any = null
): Promise<any> {
  let fullPath = "http://127.0.0.1:8000/" + path;
  let res;
  if (method == "get") {
    res = await fetch(fullPath);
  } else if (method == "post") {
    res = await fetch(fullPath, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(json),
    });
  } else {
    throw new Error("Invalid method");
  }
  return await res.json();
}
