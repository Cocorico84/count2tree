<template>
    <v-container>
        <v-layout v-if="tree !== null">
            <v-flex xs8>
                <v-card color="#C5E1A5" class="mx-auto">
                    <v-app-bar color="#D7CCC8" dark>
                        <v-card-title>{{ tree.genus }} {{ tree.specie }} {{ tree.variety }}</v-card-title>
                        <div class="flex-grow-1"></div>
                        <v-btn
                        text icon 
                        :color="color" 
                        @click="change_color"
                        >
                        <v-icon>mdi-heart</v-icon>
                        </v-btn>
                    </v-app-bar>
                    <v-card-text>{{ tree.location }}</v-card-text>
                    <v-card-text>Hauteur : {{ tree.height }} m</v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        props: ['tree'],
        data: () => ({
            color : 'grey'
        }),
        methods: {
            change_color () {  
                this.color = "pink"            
            }
        }
    };
</script>/