export type Shoe = {
  name: string;
  price: number;
  size: number;
  id: string;
};

export type ShoeWithPoints = {
  shoe: Shoe;
  points: number[][];
};

export type AnalyzeRequest = {
  id: string;
};

export type AnalyzeResponse = {
  original: ShoeWithPoints;
  similar: ShoeWithPoints[];
  today: number;
};

export type SearchRequest = {
  search: string;
};
