<template>
  <div>
  <v-container pa-5>
    <v-row justify="center" class="ma-3">
    <h2 class="title font-weight-bold">ログイン</h2>
    </v-row>
    <v-divider></v-divider>

    <validation-observer
      ref="observer"
    >
      <form @submit.prevent="submitLogin" class="py-10">
        <v-col cols="12" sm="" md="3" lg="6">
          <h3 class="headline font-weight-bold mb-5">車査定へようこそ</h3>
          <validation-provider
            v-slot="{ errors }"
            name="email"
            rules="required|max:30"
          >
            <v-text-field
              type="email"
              v-model="email"
              :counter="30"
              :error-messages="errors"
              label="email"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="password"
            rules="required|max:30"
          >
            <v-text-field
              v-model="password"
              :counter="30"
              :error-messages="errors"
              label="password"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>

        <v-row justify="center" class="ma-2 mt-5">
            <v-btn
              type="submit"
              color="pink darken-1"
              x-large
              block
              class="white--text font-weight-bold body-1"
            >
              続行する
            </v-btn>
        </v-row>
      </form>
    </validation-observer>
    <v-divider></v-divider>

    <v-row justify="center" class="ma-5">
      新規登録は<router-link to="/signup">こちら</router-link>
    </v-row>
    
  </v-container>

    <div class="push"></div>
    <BottomNavi />
  </div>
</template>

<script>
  import BottomNavi from '@/components/BottomNavi.vue'
  import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

  setInteractionMode('eager')

  extend('digits', {
    ...digits,
    message: '{_field_} needs to be {length} digits. ({_value_})',
  })

  extend('required', {
    ...required,
    message: '{_field_} can not be empty',
  })

  extend('max', {
    ...max,
    message: '{_field_} may not be greater than {length} characters',
  })

  extend('regex', {
    ...regex,
    message: '{_field_} {_value_} does not match {regex}',
  })

  extend('email', {
    ...email,
    message: 'Email must be valid',
  })

  export default {
    name: 'Home',
    data() {
      return {
        email: '',
        password: '',
        url: ''
      }
    },
    components: {
      BottomNavi,
      ValidationProvider,
      ValidationObserver,
    },
    methods: {
      submitLogin() {
        // ログイン
        this.$store.dispatch('auth/login', {
          email: this.email,
          password: this.password,
        })
        .then(() => {
          console.log('ログインしました')
          const next = this.$route.query.next || '/mypage/'
          this.$router.replace(next)
        }).catch(error => {
          console.log(error);
        })
      },
    },
  }
</script>

<style>
  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }
</style>