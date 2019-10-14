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
            </v-container>
        </v-content>
    </v-app>
</template>

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
        data: () => ({
            search : '',
            trees: [],
            items : [],
        }),
=======
>>>>>>> Stashed changes
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