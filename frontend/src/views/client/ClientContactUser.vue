<template>
  <div>
    <h1>ユーザーメッセージ</h1>

    <!-- {{mail_user[0].sender.name}}さんから受信したメッセージ：{{inbox.length}}件 -->

  {{inbox}}
  <br>
  <br>
  <br>
  <br>
  {{client_messages}}


  

    <div v-for="inbox_message in inbox" :key="inbox_message.id">
      <ul>
        <li>{{inbox_message.sender_profile.nickname}}</li>
        <li>{{inbox_message.message}}</li>
      </ul>
      <hr>
    </div>
    あああ
    いいい

    <div v-for="client_message in mail_user" :key="client_message.id">
      <ul>
        <li>{{client_message.sender_profile.nickname}}</li>
        <li>{{client_message.message}}</li>
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
        url: '/inbox/',
      })
      .then(response => this.inbox = response.data.results.filter((v1, i1, a1) => {
          return a1.findIndex(v => v1.sender_profile.nickname === v.sender_profile.nickname) === i1
        }))
      .catch(error => console.log(error));

      api({
        method: 'get',
        url: '/message/'
      })
      .then(response => this.client_messages = response.data.results.filter(client => client.sender_profile.nickname === 'takuchan'))
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