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
    </v-app>
</template>

<script>
    import axios from 'axios';
    import Tree from './components/Tree';

    export default {
        name: 'App',
        components: {
            Tree,
        },
        data: () => ({
            search : '',
            trees: [],
            items : []
        }),
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
