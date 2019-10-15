<template>
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
            </v-container>
        </v-content>
      </v-app>
</template>

<script>
    import axios from 'axios';
    import Tree from './components/Tree';

    export default {
        name: 'App',
        data: () => ({
            search : '',
            trees: [],
            items : [],
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