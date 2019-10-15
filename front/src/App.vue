<template>
<<<<<<< Updated upstream
    <v-app >
        <Search/>
        <v-content>
            <v-container>
                <v-row>
                <v-col cols="4">
                    <Favorite/>
                </v-col>
                <v-col cols="8">
                    <Login/>
                </v-col>
                <v-col cols="12">
                    <Tree :tree="tree" v-for="tree in trees" :key="tree.name"/>
                    <Sparkline/>
                    <Pagination/>
                </v-col>
                </v-row>
=======
    <v-app>
        <Search/>

        <v-content>
            <v-container>
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"

                <v-row>
                <v-col>

                    <Favorite/>
                    <Login/>
                    <Tree :tree="tree" v-for="tree in trees" :key="tree.name"/>
                    <Sparkline/>
                    <Pagination/>
<<<<<<< Updated upstream

                </v-col>
                </v-row>

>>>>>>> Stashed changes
=======

                <v-row>
                <v-col>

                    <Favorite/>
                    <Login/>
                    <Tree :tree="tree" v-for="tree in trees" :key="tree.name"/>
                    <Sparkline/>
                    <Pagination/>

                </v-col>
                </v-row>

>>>>>>> Stashed changes
=======

                </v-col>
                </v-row>

>>>>>>> Stashed changes
            </v-container>
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
        components: {
            Tree,
            Login,
            Favorite,
            Search,
            Pagination,
            Sparkline
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
            }
        }
    }
</script>