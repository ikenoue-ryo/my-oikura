<template>
  <div>
  <v-container>
    <validation-observer
      ref="observer"
    >
    <h2>来店予約</h2>
      <form @submit="submit">
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="名前"
            rules="required|max:30"
          >
            <v-text-field
              v-model="name"
              :counter="30"
              :error-messages="errors"
              label="名前"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="電話番号"
            rules="required|max:30"
          >
            <v-text-field
              v-model="tel"
              :counter="30"
              :error-messages="errors"
              label="電話番号"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="Email"
            rules="required|max:30"
          >
            <v-text-field
              v-model="email"
              :counter="30"
              :error-messages="errors"
              label="Email"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="reservation"
          >
            <v-text-field
              v-model="reservation"
              :error-messages="errors"
              label="予約日時"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="comment"
          >
            <v-text-field
              v-model="comment"
              :error-messages="errors"
              label="コメント"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        

        <v-btn
          class="mr-4"
          type="submit"
        >
          予約送信
        </v-btn>
        <v-btn @click="clear">
          クリア
        </v-btn>
      </form>
    </validation-observer>
  </v-container>

  </div>
</template>

<script>
  import axios from 'axios'
  import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  import api from '@/services/api'
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
        name: '',
        tel: '',
        email: '',
        reservation: '',
        comment: '',
      }
    },
    components: {
      ValidationProvider,
      ValidationObserver,
    },
    methods: {
      submit() {
        this.$refs.observer.validate();
        let formData = new FormData();
        let url = '/api/offers/';
        let config = {
          headers: {
            'content-type': 'multipart/form-data'
          }
        };
        formData.append('name', this.name);
        formData.append('tel', this.tel);
        formData.append('email', this.email);
        formData.append('reservation', this.reservation);
        axios.post(url, formData, config).then(response => {
          console.log(response);
          const next = '/'
          this.$router.replace(next)
        }).catch(error => {
          console.log(error);
        })
      },
      clear() {
        this.name = ''
        this.tel = ''
        this.email = ''
        this.reservation = ''
        this.comment = ''
        this.$refs.observer.reset()
      },
      submitMulchForm() {
        this.$refs.observer.validate()
        let formData = new FormData();
        let url = '/api/user_info/';

        api({
          method: 'post',
          url: url,
          data: formData,
        })
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
      },
    }
  }
</script>

<style>

</style>