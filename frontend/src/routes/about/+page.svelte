<script>
  import logoImage from "$lib/assets/logo.png";
</script>

<div class="top">
  <div class="text">
    <h1>
      <span> About </span>

      <div class="logo rev" style={`--image: url("${logoImage}")`}></div>
    </h1>
    <p>
      We are a small team of children, dedicating our lives to making the shoe
      market more profitable.
    </p>
  </div>
</div>

<style>
  .top {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .text {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    /* align-items: center; */
    width: 100%;
    max-width: 50rem;
  }
  h1 {
    font-size: 5rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  p {
    font-size: 2rem;
    line-height: 1.5;
  }

  .logo {
    background: var(--image);
    /* background-size: 400px 100px; */
    background-repeat: repeat-x;
    width: 30rem;
    background-size: 10rem 10rem;
    height: 10rem;
  }
</style>
