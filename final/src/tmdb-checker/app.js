import axios from "axios";
import fs from "fs";
import { data } from "./data.js";
const API_URL_NAME =
    "https://api.themoviedb.org/3/search/movie?api_key=008c1cd003f8a0a958f6375dfa382927&query=";
const API_URL_ID = "https://api.themoviedb.org/3/movie/";
const selected_movies = data();
const movies_ids = [];
const missing_movies = [];
const movies_with_error = [];
const selected_data = [];

const createUrlQueryName = (movie) => {
    let movie_name = `${movie.nome}`;
    let string_list = movie_name.split(" ");
    let query_string = string_list.join("+");
    return query_string;
};

const getMoviesIds = async () => {
    let counter = 0;
    await Promise.all(
        selected_movies.map(async (movie, index) => {
            let query = createUrlQueryName(movie);
            try {
                let res = await axios.get(`${API_URL_NAME}${query}`);
                counter++;
                console.log(`nome:${movie.nome} id:${res.data.results[0].id} `);
                movies_ids.push(res.data.results[0].id);
            } catch {
                console.log(`MISSING MOVIE ${movie.nome}`);
                missing_movies.push(movie.nome);
            }
            if (counter >= 40) {
                setTimeout(() => {
                    counter = 0;
                }, 10000);
            }
        })
    );
};

const getMoviesData = async () => {
    await Promise.all(
        movies_ids.map(async (id, index) => {
            let url_complement = `${id}?api_key=008c1cd003f8a0a958f6375dfa382927&language=en-US`;
            try {
                let res = await axios.get(`${API_URL_ID}${url_complement}`);
                console.log(
                    `id:${id} nome:${res.data.original_title} lancamento:${
                        res.data.release_date
                    }  estudios:${
                        res.data.production_companies.length > 0
                            ? "true"
                            : "false"
                    }`
                );
                if (res.data.release_date && res.data.production_companies) {
                    selected_data.push({
                        tmdb_id: id,
                        imdb_id: res.data.imdb_id,
                        production_companies: res.data.production_companies,
                        release_date: res.data.release_date,
                    });
                }
            } catch {
                console.log(`MOVIE WITH ERROR ${id}`);
                movies_with_error.push(id);
            }
        })
    );
};

const createData = async () => {
    let missing_movies_obj = { missing_movies: missing_movies };
    let selected_data_obj = { data: selected_data };
    let missing_movies_json = JSON.stringify(missing_movies_obj);
    let selected_data_json = JSON.stringify(selected_data_obj);
    fs.writeFileSync("missing-movies.json", missing_movies_json);
    fs.writeFileSync("selected-data.json", selected_data_json);

    console.log("PROCESS COMPLETED");
};

const exec = async () => {
    console.log(selected_movies.length);
    await getMoviesIds();
    await getMoviesData();
    await createData();
};

exec();
