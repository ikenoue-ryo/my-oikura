<template>
  <div>
    <v-card
      max-width="450"
      class="mx-auto"
    >
      <v-toolbar>
        <TopNavi />
        <v-toolbar-title class="ml-10">Message</v-toolbar-title>
        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>

      <v-list three-line>
        <template v-for="(item, index) in inbox">
          <v-subheader
            v-if="item.header"
            :key="item.header"
            v-text="item.header"
          ></v-subheader>

          <v-divider
            v-else-if="item.divider"
            :key="index"
            :inset="item.inset"
          ></v-divider>

          <v-list-item
            v-else
            :key="item.title"
            v-ripple
          >
            <v-list-item-avatar>
              <v-img :src="item.sender_profile.img"></v-img>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-html="item.message"></v-list-item-title>
              <!-- <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle> -->
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card>

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
      .then(response => this.inbox = response.data.results.filter(user => user.sender_profile.nickname === this.$route.params['username'] || user.receiver_profile.nickname === this.$route.params['username']))
      .catch(error => console.log(error));

      // api({
      //   method: 'get',
      //   url: '/message/'
      // })
      // .then(response => this.client_messages = response.data.results.filter(client => client.sender_profile.nickname === 'takuchan'))
      // .catch(error => console.log(error))
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