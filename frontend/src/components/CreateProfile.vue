<template>
  <div>
    <form @submit="postsubmit">
				<h2>Create Profile</h2>
				<div class="form-group">
				<label for="first_name">NickName</label>
				<input type="text" class="form-control" v-model="nickname" placeholder="nick_name">
				</div>					
				<div class="form-group">
				<label for="last_name">postal_code</label>
				<input type="text" class="form-control" v-model="postal_code" placeholder="postal_code">
        </div>

        <v-btn
          class="mr-4"
          type="submit"
        >
          送信
        </v-btn>
			</form>
  </div>
</template>

<script>
  import api from '@/services/api'

  export default {
    name: 'CreateProfile',
    data() {
      return {
        nickname: null,
        postal_code: null,
        uploadFile: null,
        url: '',
        id : this.$store.getters['auth/id'],
        name : this.$store.getters['auth/username'],
      }
    },
    methods: {
      selectedFile(e) {
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
        this.url = URL.createObjectURL(this.uploadFile);
        this.$refs.preview.value = "";
      },
      postsubmit() {
        let formData = new FormData();
        let url = '/api/v1/api/profile/';
        // let config = {
        //   headers: {
        //     'content-type': 'multipart/form-data'
        //   }
        // };
        formData.append('nickname', this.nickname);
        formData.append('postal_code', this.postal_code);
        // formData.append('img', this.uploadFile);
        formData.append('user.id', 4);
        formData.append('user.email', 'kou@gmail.com');
        formData.append('user.name', 'kou');
        api({
          method: 'post',
          url: url,
          data: formData,
        })
        .then(response => {
          console.log(response.data)
          this.$router.go('/')
        })
        .catch(error => console.log(error))
      },
    }
  }
</script>
