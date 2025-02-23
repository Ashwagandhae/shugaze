import type { PageLoad } from "../$types";
import { search } from "$lib/request";

export const load: PageLoad = async ({ params }) => {
  let slug = (params as any).slug;

  // get data about shoe

  let results = await search({ search: slug });
  return {
    results,
    search: slug,
  };
};
