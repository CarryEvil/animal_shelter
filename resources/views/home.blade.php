@extends('_layouts.default')

@section('content')
	<div id="title" style="text-align: center;">
		<h1>動物收容所資訊平台</h1>
		<div style="padding: 5px; font-size: 16px;">{{ Inspiring::quote() }}</div>
	</div>
	<hr>
	<div id="content">
		<ul>
			@foreach ($animals as $animal)
			<li style="margin: 50px 0;">
				<div class="title">
					<a href="{{ URL('animals/'.$animal->id) }}">
						<h4>{{ $animal->animal_place }} {{ $animal->animal_kind }}</h4>
					</a>
				</div>
				<div class="body">
					<p>{{ $animal->animal_remark }}</p>
				</div>
			</li>
			@endforeach
		</ul>
	</div>
	<?php echo $animals->render(); ?>
@endsection