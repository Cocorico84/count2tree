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

<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
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

            </v-container>
        </v-content>
    </v-app>
</template>

>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
<script>
    import axios from 'axios';
    import Tree from './components/Tree';
    import Login from './components/Login';
    import Favorite from './components/Favorite';
    import Search from './components/Search';
    import Pagination from './components/Pagination';
    import Sparkline from './components/Sparkline';

    export default {
        name: 'App',
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> (no branch): Auto stash before checking out "Favorite"
        data: () => ({
            search : '',
            trees: [],
            items : [],
        }),
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
        components: {
            Tree,
            Login,
            Favorite,
            Search,
            Pagination,
            Sparkline
        },
    }
</script>