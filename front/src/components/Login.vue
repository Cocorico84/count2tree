<template>
    <v-app>
    <v-card width="400" class="pa-2">
      <v-card-title class="pb-0">
        <h1>Login</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field 
            label="Username" 
            prepend-icon="mdi-account-circle"
          />
          <v-text-field 
            :type="showPassword ? 'text' : 'password'" 
            label="Password"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
          />
        </v-form>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="success">Register</v-btn>
        <v-btn color="info">Login</v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
export default {
    data: () => ({
        showPassword: false,
        username: null,
        password: null
        }),
        methods : {
          searchTree() {
              axios.get('http://localhost:8000/api/v1/trees')
              .then((response) => {this.trees = response.data
              });
          }
        },
        showPassword: false,
          register() {
              let param = {
                username: this.username,
                password:this.password
                  }
              axios.post('http://localhost:8000/api/v1/user',param)
              .then((response) => {this.user = response.data
              });
              if (this.$refs.form.validate()) {
              console.log('User validated !') }
              },
              login() {

              }
          }
</script>