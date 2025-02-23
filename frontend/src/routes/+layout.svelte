<script>
  import "../global.css";
  import logoImage from "$lib/assets/logo.png";
</script>

<main>
  <header>
    <div class="headerName">
      <img src={logoImage} alt="logo" class="logo" />
      <h1><a href="/">ShuGaze</a></h1>
    </div>
    <div class="links">
      <a href="/about">About</a>
    </div>
  </header>
  <div class="scroll">
    <slot></slot>
  </div>
</main>

<style>
  header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 1rem;
    align-items: center;
    position: absolute;
    width: calc(100vw - 2rem);
    box-sizing: border-box;

    z-index: 9999;
    box-shadow: 0px 0px 30px rgba(61, 61, 61, 0.2);
    border-radius: 0 0 1rem 1rem;
    height: 5rem;
    left: 1rem;
    background: white;
  }

  div.links {
    display: flex;
    flex-direction: row;
    gap: 1rem;
  }
  a {
    color: black;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  .scroll {
    padding-top: 5rem;
    padding-bottom: 5rem;
    box-sizing: border-box;
    overflow: scroll;
    width: 100vw;
    height: calc(100vh);
  }
  .headerName {
    display: flex;
    flex-direction: row;
    gap: 0.5rem;
  }
  .logo {
    width: 4.5rem;
    height: 4.5rem;
  }
</style>
