<template>
  <div>
    <Header />
    <GlobalMenu />

    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
        <v-col cols="12" sm="6" md="4" lg="3">
        a
        </v-col>
      </v-row>
    </v-container>

  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'

  export default Vue.extend({
    name: 'Home',

    components: {
      Header,
      GlobalMenu,
    },
  })
</script>

<style>
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>