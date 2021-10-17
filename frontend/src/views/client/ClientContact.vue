<template>
  <div>
    <ClientHeader />
    <ClientGlobalMenu />
    <h1>加盟店問い合わせページ</h1>

    受信したメッセージ：{{inbox.length}}件

    <div v-for="inbox_message in inbox" :key="inbox_message.id">
      <ul>
        <li>送信者：<router-link :to="`/client/contact/${inbox_message.sender.name}`">{{inbox_message.sender.name}}</router-link></li>
        <li>{{inbox_message.message}}</li>
      </ul>
      <hr>
    </div>

  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientGlobalMenu from '@/components/client/ClientGlobalMenu.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        inbox: '',
        client_messages: [],
      }
    },
    components: {
      ClientHeader,
      ClientGlobalMenu,
    },
    mounted(){
      api({
        method: 'get',
        url: '/inbox/',
      })
      .then(response => this.inbox = response.data.results.filter((v1, i1, a1) => {
          return a1.findIndex(v => v1.sender.name === v.sender.name) === i1
        }))
      .catch(error => console.log(error));
      
      // api({
      //   method: 'get',
      //   url: '/api/v1/api/message/'
      // })
      // .then(response => this.client_messages = response.data)
      // .catch(error => console.log(error))
    },
    computed: {
      id() {
        return this.$store.getters['auth/id']
      },
    }
  }
</script>

<style>

</style>