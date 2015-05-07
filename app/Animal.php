<?php namespace App;

use Illuminate\Database\Eloquent\Model;

class Animal extends Model {

  public function hasManyComments()
  {
    return $this->hasMany('App\Comment', 'animal_id', 'id');
  }

}
