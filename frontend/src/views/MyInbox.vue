<template>
  <div>
    <template>
      <v-card
        max-width="450"
        class="mx-auto"
      >
        <v-toolbar>
          <TopNavi />
          <v-toolbar-title class="ml-10">Inbox</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-row class="ma-2">
          <v-col>
            <h2 class="title">{{mail_user.length}}件のメッセージがあります</h2>
          </v-col>
        </v-row>
        <v-list three-line>
          <template v-for="inbox_message in mail_user">
            <v-list-item
              :key="inbox_message.id"
              :href="`/inbox/${inbox_message.sender_profile.nickname}`"
              v-ripple
            >
              <v-list-item-avatar>
                <v-img :src="inbox_message.sender_profile.img"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="inbox_message.message"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </template>

    <BottomNavi />

  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
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
      TopNavi,
      BottomNavi
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