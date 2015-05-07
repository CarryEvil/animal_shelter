<?php namespace App\Http\Controllers\Admin;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use Illuminate\Http\Request;

use App\Animal;

use Redirect, Input, Auth;

class AnimalsController extends Controller {

	/**
	 * Show the form for creating a new resource.
	 *
	 * @return Response
	 */
	public function create()
	{
		return view('admin.pages.create');
	}

	/**
	 * Store a newly created resource in storage.
	 *
	 * @return Response
	 */
	public function store(Request $request)
	{
		$this->validate($request, [
			'animal_place' => 'required',
			'animal_remark' => 'required',
		]);

		$animal = new Animal;
		$animal->animal_place = Input::get('animal_place');
		$animal->animal_remark = Input::get('animal_remark');

		if ($animal->save()) {
			return Redirect::to('admin');
		} else {
			return Redirect::back()->withInput()->withErrors('儲存失敗！');
		}

	}

	/**
	 * Show the form for editing the specified resource.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function edit($id)
	{
		return view('admin.pages.edit')->withAnimal(Animal::find($id));
	}

	/**
	 * Update the specified resource in storage.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function update(Request $request,$id)
	{
		$this->validate($request, [
			'animal_place' => 'required',
			'animal_remark' => 'required',
		]);

		$animal = Animal::find($id);
		$animal->animal_place = Input::get('animal_place');
		$animal->animal_remark = Input::get('animal_remark');

		if ($animal->save()) {
			return Redirect::to('admin');
		} else {
			return Redirect::back()->withInput()->withErrors('儲存失敗！');
		}
	}

	/**
	 * Remove the specified resource from storage.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function destroy($id)
	{
		$animal = Animal::find($id);
		$animal->delete();

		return Redirect::to('admin');
	}

}