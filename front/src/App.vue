<template>
    <v-app>
        <v-app-bar 
            app
            src="./assets/arbre.jpg" 
            aspect-ratio="1.7"
            >
            <v-toolbar-title class="mx-5 my-auto">
                <v-layout class="mx-5">

                <v-flex xs10 >
                    <v-select
                            solo
                            label="Search by location"
                            :items="items"                
                            prepend-inner-icon="mdi-magnify"
                            v-model="search">
                        >                                  
                    </v-select>
                </v-flex>
                <v-flex xs2 class="ml-2 mt-1">
                    <v-btn block large @click="searchTree">Search</v-btn>
                </v-flex>
            </v-layout> 
            </v-toolbar-title>
        </v-app-bar>
        <v-content>
            <Tree :tree="tree" v-for="tree in trees" :key="tree.name"/>
        </v-content>


        <v-card max-width="475" class="pt-2 ms-2">
            <v-toolbar color="teal" dark>
                <v-toolbar-title>Favorites</v-toolbar-title>
            </v-toolbar>
                <v-list>
                    <v-list-item-group
                        v-model="settings"
                        multiple
                        active-class=""
                    >
                        <v-list-item>
                        <template v-slot:default="{ active }">
                            <v-list-item-action>
                            <v-checkbox v-model="active"></v-checkbox>
                            </v-list-item-action>
                            <v-list-item-content>
                            <v-list-item-title>Notifications</v-list-item-title>
                            </v-list-item-content>
                        </template>
                        </v-list-item>
                    </v-list-item-group>
                    </v-list>
        </v-card>

  <v-app>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title class="pb-0">
        <h1>Login</h1>
      </v-card-title>
      <v-card-text>
        <v-form ref="form">
          <v-text-field
            v-model='username'
            label="Username" 
            prepend-icon="mdi-account-circle"
          />
          <v-text-field 
            v-model="password"
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
        <v-btn color="success" @click='register'>Register</v-btn>
        <v-btn color="info" @click='login'>Login</v-btn>
      </v-card-actions>
    </v-card>
  </v-app>

<v-sparkline
    :labels="value"
    :value="value"
    :gradient="gradients"
    :smooth="radius || false"
    :padding="padding"
    :line-width="width"
    :stroke-linecap="lineCap"
    :gradient-direction="gradientDirection"
    :fill="fill"
    :type="type"
    :auto-line-width="autoLineWidth"
    auto-draw
></v-sparkline>

    </v-card-text>
<v-card-text>
      <div class="display-1 font-weight-thin">Trees in Paris</div>
    </v-card-text>

        <v-content>
            <Tree :tree="tree" v-for="tree in trees" :key="tree.name"/>
                <div class="text-center">
                    <v-container>
                    <v-row justify="center">
                        <v-col cols="8">
                        <v-container class="max-width">
                            <v-pagination
                            v-model="page"
                            class="my-4"
                            :length="5"
                            ></v-pagination>
                        </v-container>
                        </v-col>
                    </v-row>
                    </v-container>
                </div>
        </v-content>

      </v-app>
</template>





<script>
    import axios from 'axios';
    import Tree from './components/Tree';

    const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]
    export default {
        name: 'App',
        components: {
            Tree,
        },
        data: () => ({
            search : '',
            trees: [],
            items : [],
            page: 1,
            selected : [],
            showPassword: false,
            username: '',
            password:'',
            user : {},
            width: 2,
            radius: 10,
            padding: 8,
            lineCap: 'round',
            gradient: gradients[5],
            value: [],
            gradientDirection: 'top',
            gradients,
            fill: false,
            type: 'trend',
            autoLineWidth: false,
        }),
        created() {
            this.searchTree();
        },
        methods : {
            searchTree() {
                let params = {query : this.search};
                axios.get('http://localhost:8000/api/v1/trees',{params:params})
                .then((response) => {this.trees = response.data
                });
            
                axios.get('http://localhost:8000/api/v1/locations')
                .then((response) => {this.items = response.data
                });

                axios.get('http://localhost:8000/api/v1/height',{params: params})
                .then((response) => {this.value = response.data
                });
            },
            register(){
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
    }
</script>
