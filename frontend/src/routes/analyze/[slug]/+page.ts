import type { PageLoad } from "./$types";
import { analyze } from "$lib/request";

export const load: PageLoad = async ({ params }) => {
  let slug = params.slug;

  // get data about shoe

  let res = await analyze({ id: slug });
  return {
    originalShoe: res.original,
    similarShoes: res.similar,
    today: res.today,
  };
};
