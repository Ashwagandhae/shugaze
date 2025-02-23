import { error } from "@sveltejs/kit";
import type { PageLoad } from "./$types";
import type { Shoe } from "$lib/model";
import { trending } from "$lib/request";

export const load: PageLoad = async ({ params }) => {
  let trendingShoes = await trending();
  return {
    trendingShoes,
  };
};
