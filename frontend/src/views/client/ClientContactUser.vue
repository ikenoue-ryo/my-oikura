<template>
  <div>
    <ClientHeader />
    <ClientGlobalMenu />
    <h1>ユーザーメッセージ</h1>

    {{mail_user[0].sender.name}}さんから受信したメッセージ：{{inbox.length}}件



    <div v-for="inbox_message in mail_user" :key="inbox_message.id">
      <ul>
        <li>{{inbox_message.message}} {{inbox_message.created_at}}</li>
      </ul>
      <hr>
    </div>

    {{client_messages[0].message}}  {{client_messages[0].message}}<br>
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
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/inbox/',
      })
      .then(response => this.inbox = response.data.results.filter(user_inbox => user_inbox.sender.name === this.$route.params.username))
      .catch(error => console.log(error));
      
      api({
        method: 'get',
        url: '/api/v1/api/message/'
      })
      .then(response => this.client_messages = response.data.results.filter(messages => messages.receiver.name === this.$route.params.username))
      .catch(error => console.log(error))
    },
    computed: {
      username() {
        return this.$store.getters['auth/username']
      },
      mail_user() {
        const mail_user = this.inbox
        return mail_user;
      }
    }
  }
</script>

<style>

</style>