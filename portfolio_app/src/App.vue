<template>
  <div id="app">
    <div id="nav">
      <router-link to="/index">Portfolio</router-link> |
      <router-link to="/create">Add entry</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  color: #42b983;
}

#nav a {
  font-weight: bold;
  color: #42b983;
}

#nav a.router-link-exact-active {
  color: #33976a;
}

    body {
        background: #333;
        color: #fff;
        text-align: center;
        padding: 10px;
    }

</style>
