<template>
  <div>
    <h1>ユーザーメッセージ</h1>

    <!-- {{mail_user[0].sender.name}}さんから受信したメッセージ：{{inbox.length}}件 -->

  {{client_messages}}

    <div v-for="inbox_message in mail_user" :key="inbox_message.id">
      <ul>
        <li>{{inbox_message.message}}</li>
      </ul>
      <hr>
    </div>

    <!-- {{client_messages[0].message}}<br> -->
  </div>
</template>

<script>
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
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/message/'
      })
      .then(response => this.client_messages = response.data.results)
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