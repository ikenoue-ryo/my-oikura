<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data() {
    return {

    }
  },
};
</script>

<style>
  .v-application{
      font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif;
  }
  a {
    text-decoration: none;
  }
  ul li {
    list-style: none;
  }
</style>