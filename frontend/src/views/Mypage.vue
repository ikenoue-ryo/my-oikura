<template>
  <div>
    <Header />
    <GlobalMenu />
      <template>
        <p>{{ mypage.email }}</p>
        <p>{{ mypage.id }}</p>
        <p>{{ mypage.username }}</p>
      </template>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import axios from 'axios'
  import api from '@/services/api'

  export default Vue.extend({
    name: 'Home',
    data: () => ({
      mypage: ''
    }),
    components: {
      Header,
      GlobalMenu,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));
    },
  })
</script>

<style>

</style>