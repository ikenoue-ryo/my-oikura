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

          <!-- <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn> -->
        </v-toolbar>

      <v-container class="pa-8">
        <v-row class="mt-5">
          <v-col>
            <h3 class="my-3">メッセージ件数 ({{mail_user.length}}件)</h3>
            <div v-if="mail_user">
              以下の店舗とメッセージをしています。
              <template>
                <div
                  class="mt-3"
                  tile
                >
                  <v-list flat>
                    <v-list-item-group
                      v-model="selectedItem"
                      color="primary"
                    >
                      <v-list-item
                        v-for="(inbox_message, i) in mail_user"
                        :key="i"
                        class="pa-0"
                        :href="`/client/contact/${inbox_message.sender_profile.user.name}`"
                      >
                        <v-list-item-icon class="mr-3">
                          <v-img :src="inbox_message.sender_profile.img" width="40" height="40" :class="`rounded-circle`"></v-img>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title v-text="inbox_message.message"></v-list-item-title>
                          <!-- <v-list-item-subtitle>車種： {{inbox_message.offer.item_name}}</v-list-item-subtitle>
                          <v-list-item-subtitle>Price：{{inbox_message.value|priceLocaleString}} 円</v-list-item-subtitle> -->
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </div>
              </template>
            </div>
            <div v-else>
              まだやりとりがありません。
            </div>
          </v-col>
        </v-row>
      </v-container>

      </v-card>
    </template>
  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        inbox: '',
        client_messages: [],

        items: [
          { header: 'Today' },
          {
            avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
            title: 'Brunch this weekend?',
            subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
          },
          { divider: true, inset: true },
          {
            avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
            title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
            subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
          },
          { divider: true, inset: true },
          {
            avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
            title: 'Oui oui',
            subtitle: '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
          },
          { divider: true, inset: true },
          {
            avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
            title: 'Birthday gift',
            subtitle: '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
          },
          { divider: true, inset: true },
          {
            avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
            title: 'Recipe to try',
            subtitle: '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
          },
        ],
      }
    },
    components: {
      TopNavi
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