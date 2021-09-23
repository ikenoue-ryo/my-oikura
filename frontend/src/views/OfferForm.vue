<template>
  <div>
    <Header />
    <GlobalMenu />

    <h1>Step: {{ stepNumber }}</h1>
    <FormName v-if="stepNumber === 1" @update="updateForm" />
    <FormContact v-if="stepNumber === 2" @update="updateForm" />
    <FormBirthday v-if="stepNumber === 3" @update="updateForm" />

    <FormConfirm v-if="stepNumber === 4" :form="form" />

    <button @click="backStep" v-show="stepNumber != 1">Back</button>
    <button @click="nextStep" v-show="stepNumber != 4">Next</button>

    <pre><code>{{form}}</code></pre>

     <v-container>
    <validation-observer
      ref="observer"
    >
      <form @submit="submitMulchForm">
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="form.first_name"
            rules="required|max:10"
          >
            <v-text-field
              v-model="form.first_name"
              :counter="10"
              :error-messages="errors"
              label="first_name"
              required
              :value=form.first_name
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="form.last_name"
            rules="required|max:10"
          >
            <v-text-field
              v-model="form.last_name"
              :counter="10"
              :error-messages="errors"
              label="last_name"
              required
              :value=form.last_name
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="form.email"
            rules="required|max:20"
          >
            <v-text-field
              v-model="form.email"
              :counter="20"
              :error-messages="errors"
              label="email"
              required
              :value=form.email
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="form.tel"
            rules="required|max:10"
          >
            <v-text-field
              v-model="form.tel"
              :counter="10"
              :error-messages="errors"
              label="tel"
              required
              :value=form.tel
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="birthday"
            rules="required|max:10"
          >
            <v-text-field
              v-model="form.birthday"
              :counter="10"
              :error-messages="errors"
              label="form.birthday"
              required
              :value=form.birthday
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

  <v-container>
    <validation-observer
      ref="observer"
    >
      <form @submit="submit">
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="商品名"
            rules="required|max:10"
          >
            <v-text-field
              v-model="item_name"
              :counter="10"
              :error-messages="errors"
              label="商品名"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            name="製造年"
            rules="required|max:4"
          >
            <v-text-field
              v-model="item_date"
              :counter="4"
              :error-messages="errors"
              label="製造年"
              required
            ></v-text-field>
          </validation-provider>
        </v-col>
        <v-col cols="12" sm="" md="3" lg="6">
          <input @change="selectedFile" type="file" name="file" ref="preview">
        </v-col>
        <div v-if="url" style="postion:relative">
          <div style="position:absolute" @click="deletePreview">X</div>
          <img :src="url">
        </div>
          <!-- <validation-provider
            v-slot="{ errors }"
            name="select"
            rules="required"
          >
            <v-select
              v-model="select"
              :items="items"
              :error-messages="errors"
              label="Select"
              data-vv-name="select"
              required
            ></v-select>
          </validation-provider>
        </v-col> -->
        <v-col cols="12" sm="" md="3" lg="6">
          <validation-provider
            v-slot="{ errors }"
            rules="required"
            name="checkbox"
          >
            <v-checkbox
              v-model="checkbox"
              :error-messages="errors"
              value="1"
              label="利用規約に同意"
              type="checkbox"
              required
            ></v-checkbox>
          </validation-provider>
        </v-col>

        <v-btn
          class="mr-4"
          type="submit"
        >
          送信
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
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import FormName from '@/components/FormName.vue'
  import FormContact from '@/components/FormContact.vue'
  import FormConfirm from '@/components/FormConfirm.vue'
  import FormBirthday from '@/components/FormBirthday.vue'
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
        item_name: '',
        item_date: '',
        image: '',
        select: null,
        // items: [
        //   'Item 1',
        //   'Item 2',
        //   'Item 3',
        //   'Item 4',
        // ],
        checkbox: null,
        offers: '',
        uploadFile: null,
        url: '',
        stepNumber: 1,
        form: {
          first_name: null,
          last_name: null,
          email: null,
          tel: null,
          birthday: null,
        }
      }
    },
    components: {
      Header,
      GlobalMenu,
      ValidationProvider,
      ValidationObserver,
      FormName,
      FormContact,
      FormConfirm,
      FormBirthday,
    },
    methods: {
      selectedFile(e) {
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
        this.url = URL.createObjectURL(this.uploadFile);
        this.$refs.preview.value = "";
      },
      submit() {
        this.$refs.observer.validate();
        let formData = new FormData();
        let url = '/api/offers/';
        let config = {
          headers: {
            'content-type': 'multipart/form-data'
          }
        };
        formData.append('item_name', this.item_name);
        formData.append('item_date', this.item_date);
        formData.append('image', this.uploadFile);
        axios.post(url, formData, config).then(response => {
          console.log(response);
          const next = '/'
          this.$router.replace(next)
        }).catch(error => {
          console.log(error);
        })
      },
      clear() {
        this.item_name = ''
        this.item_date = ''
        this.image = ''
        // this.select = null
        this.checkbox = null
        this.$refs.observer.reset()
      },
      deletePreview() {
        this.url = '';
        URL.revokeObjectURL(this.url);
      },
      updateForm(formData) {
        Object.assign(this.form, formData)
      },
      backStep() {
        this.stepNumber--;
      },
      nextStep() {
        this.stepNumber++;
      },
      submitMulchForm() {
        this.$refs.observer.validate()
        let formData = new FormData();
        let url = '/api/user_info/';

        formData.append('first_name', this.form.first_name);
        formData.append('last_name', this.form.last_name);
        formData.append('email', this.form.email);
        formData.append('tel', this.form.tel);
        formData.append('birthday', this.form.birthday);

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
  ul li {
    display: inline-block;
    margin: 10px
  }
</style>