<?php namespace App\Http\Controllers;

use App\Animal;
use Illuminate\Support\Facades\DB;

class HomeController extends Controller {

	public function index()
	{
		return view('home')->withAnimals(Animal::orderBy('animal_opendate','desc')->paginate(10));
	}

}