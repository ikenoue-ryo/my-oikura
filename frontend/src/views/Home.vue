<template>
  <div>
    <Header />
    <GlobalMenu />

    <v-container>
      <v-row>
        <v-col>
        <v-container>
          <v-btn
            depressed
            color="primary"
            x-large
            href="offer-form"
          >
            一括査定スタート
          </v-btn>
        </v-container>
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