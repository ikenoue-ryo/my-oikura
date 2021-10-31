<template>
  <div>
    <Header />
    <GlobalMenu />
    <br>
    <template>
      <v-row>
        <v-btn href="/client-shop/tokyo/">
          東京
        </v-btn>
        <v-btn href="/client-shop/fukuoka/">
          福岡
        </v-btn>
        <v-btn href="/client-shop/kanagawa/">
          神奈川
        </v-btn>
        <v-btn href="/client-shop/chiba/">
          千葉
        </v-btn>
      </v-row>
    </template>


  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import api from '@/services/api'

  export default {
    name: 'Mypage',
    data() {
      return {

      }
    },
    components: {
      Header,
      GlobalMenu,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));
    },
    computed: {

    }
  }
</script>

<style>

</style>