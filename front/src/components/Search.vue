<template>
    <v-app-bar 
    app
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> (no branch): Auto stash before checking out "Favorite"
    src="/home/coco/PycharmProjects/Count2tree2/front/src/assets/arbre.jpg"
=======
    src="/home/coco/PycharmProjects/Count2tree2/front/src/assets/arbre.jpg" 
>>>>>>> Stashed changes
=======
    src="/home/coco/PycharmProjects/Count2tree2/front/src/assets/arbre.jpg" 
>>>>>>> Stashed changes
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
=======
    src="/home/coco/PycharmProjects/Count2tree2/front/src/assets/arbre.jpg" 
>>>>>>> Stashed changes
=======
    src="/home/coco/PycharmProjects/Count2tree2/front/src/assets/arbre.jpg" 
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
    aspect-ratio="1.7"
    color="light-green"
    >
        <v-toolbar-title class="mx-5 my-auto">
            <v-layout class="mx-5">
            <v-flex xs10 >
                <v-select
                        clearable
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
</template>

<script>
    import axios from 'axios';
    import Tree from '/home/coco/PycharmProjects/Count2tree2/front/src/components/Tree';

export default {
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
        components: {
            Tree,
        },
>>>>>>> Stashed changes
=======
        components: {
            Tree,
        },
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
=======
        components: {
            Tree,
        },
>>>>>>> Stashed changes
=======
        components: {
            Tree,
        },
>>>>>>> Stashed changes
        data: () => ({
            search : '',
            trees: [],
            items : [],
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
            }
        }
}
</script>