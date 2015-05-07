@extends('app')

@section('content')
<div class="container">
  <div class="row">
    <div class="col-md-10 col-md-offset-1">
      <div class="panel panel-default">
        <div class="panel-heading">管理後台</div>

        <div class="panel-body">

          @foreach ($animals as $animal)
            <hr>
            <div class="animal">
              <h4>{{ $animal->animal_place }} {{ $animal->animal_kind }}</h4>
              <div class="content">
                <p>
                  {{ $animal->animal_opendate }}
                  {{ $animal->animal_remark }}
                </p>
              </div>
            </div>
            <a href="{{ URL('admin/animals/'.$animal->id.'/edit') }}" class="btn btn-success">編輯</a>

            <form action="{{ URL('admin/animals/'.$animal->id) }}" method="POST" style="display: inline;">
              <input name="_method" type="hidden" value="DELETE">
              <input type="hidden" name="_token" value="{{ csrf_token() }}">
              <button type="submit" class="btn btn-danger">刪除</button>
            </form>
          @endforeach
        </div>
      </div>
      <?php echo $animals->render(); ?>
    </div>
  </div>
</div>
@endsection