const axios = require('axios');

supercell = axios.create({
	baseURL: 'https://api.clashroyale.com/v1',
	headers: {"Authorization": `Bearer ${process.env.KEY}`}
});

module.exports = supercell;