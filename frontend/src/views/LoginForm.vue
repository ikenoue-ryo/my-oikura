<template>
  <div>
    <Header />
    <GlobalMenu />

  <h2>ログイン</h2>
  <v-container>
    <validation-observer
      ref="observer"
    >
      <form @submit.prevent="submitLogin">
        <v-col cols="12" sm="" md="3" lg="6">
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

        <v-btn
          class="mr-4"
          type="submit"
        >
          送信
        </v-btn>
      </form>
    </validation-observer>
  </v-container>

  サインアップは<router-link to="/signup">こちら</router-link>


  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
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
      Header,
      GlobalMenu,
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
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>