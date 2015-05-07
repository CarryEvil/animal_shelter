<?php namespace App\Http\Controllers;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use Illuminate\Http\Request;

use App\Animal;

class AnimalsController extends Controller {

  public function show($id)
  {
    return view('animals.show')->withAnimal(Animal::find($id));
  }

}
