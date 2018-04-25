<html>
	<body>
		<font size="5" face="Times" color="black">
			<h1> Bibioteca para usar a API do TWITTER. </h1>
			<ul><h2> Funções </h2>
				<li> Fazer publicações no Twitter.</li>
				<li> Fazer buscas no Twitter.</li>
			</ul>
			<ul><h2> Como usar? </h2>
				<li type="1"><h3> Importar a biblioteca</h3></li>
					<font color="green" size="3"<p> From biblioteca_twitter import Twitter</p></font>
				<li type="1"><h3> Coloca o consumer_Key, consumer_Secret, token_key e token_secret do twitter</h3></li>
					<font color="green" size="3"<p> link: https://apps.twitter.com/app/13500222/keys </p></font>
				<li type="1"><h3>Colocar as keys nas variáveis</h3></li>
					<font color="green" size="3"<p> consumer_Key, consumer_Secret, token_Key e token_Secret </p></font>
				<li type="1"><h3>Instânciar a classe Twitter e defini seus parâmetros</h3></li>
					<font color="green" size="3"<p> twitter = Twitter(consumer_Key, consumer_Secret, token_Key, token_Secret)</p></font>
				<li type="1"><h3>Publicar</h3></li>
					<font color="green" size="3"<p> publicar = twitter.novoTweet('Olá Universo')</p></font>
				<li type="1"><h3>Buscar</h3></li>
					<font color="green" size="3"<p> (1- Texto da pesquisa, 2- Idioma)</p></font>
					<font color="green" size="3"<p> pesquisa = twitter.search('Cajazeiras', 'pt')</p></font>
				<li type="1"><h3 font="color="green"">Imprimir o resultado da pesquisa</h3></li>
					<font color="green" size="3"<p> for resultado in pesquisa:</p></font>
					<font color="green" size="3"<p> print(resultado['text'])</p></font>
					<font color="green" size="3"<p> print(resultado['user']['screen_name'])</p></font>	
			</ul>
		</font>
	</body>
</html>
