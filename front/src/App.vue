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
    import Login from './components/Login';
    import Favorite from './components/Favorite';
    import Search from './components/Search';
    import Pagination from './components/Pagination';
    import Sparkline from './components/Sparkline';

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
    }
</script>